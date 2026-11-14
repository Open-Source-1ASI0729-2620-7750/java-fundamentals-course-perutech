"""Comprueba HTTP sin confundir disponibilidad con revisión audiovisual."""
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import re
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def check(url):
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(request, timeout=18) as response:
            content = response.read(2500000).decode('utf-8', errors='replace')
            result = {'url': url, 'http': response.status, 'final_url': response.url}
            if 'youtu' in url:
                lengths = re.findall(r'"lengthSeconds"\s*:\s*"(\d+)"', content)
                result['length_seconds_in_response'] = sorted(set(lengths))
                for marker in ('var ytInitialPlayerResponse = ', 'ytInitialPlayerResponse = '):
                    if marker in content:
                        try:
                            player, _ = json.JSONDecoder().raw_decode(content.split(marker, 1)[1])
                            details = player.get('videoDetails', {})
                            result['video_id'] = details.get('videoId')
                            result['title'] = details.get('title')
                            result['length_seconds'] = details.get('lengthSeconds')
                            result['playability_status'] = player.get('playabilityStatus', {}).get('status')
                            break
                        except (ValueError, TypeError):
                            pass
                result['note'] = 'HTTP no confirma reproducción, contenido ni privacidad.'
            else:
                result['note'] = 'HTTP no confirma código precargado ni ejecución en navegador.'
            return result
    except Exception as error:
        return {'url': url, 'http': getattr(error, 'code', None), 'error': str(error), 'note': 'Requiere comprobación manual.'}


if __name__ == '__main__':
    content = (ROOT / 'course-plan.md').read_text(encoding='utf-8')
    urls = sorted(set(re.findall(r'\]\((https?://[^)]+)\)', content)))
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(check, urls))
    path = ROOT / 'verification/links-results.json'
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps({'prepared_date': '2026-11-14', 'method': 'GET anónimo; no reproducción audiovisual ni sesión de editor', 'results': results}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for row in results:
        print(row['url'], row.get('http'), row.get('error', 'GET completado'))
