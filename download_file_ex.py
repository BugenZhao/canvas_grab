from download_file import download_file as df
from retrying import retry
from colorama import Fore, Style
from pathlib import Path

TIMEOUT = 3
ATTEMPT = 5


def need_retrying(exception):
    return not isinstance(exception, KeyboardInterrupt)


@retry(retry_on_exception=need_retrying, stop_max_attempt_number=ATTEMPT)
def download_file(url, desc, filename, verbose=False):
    try:
        ret = df(url, desc, filename, verbose, req_timeout=TIMEOUT)
    except KeyboardInterrupt:
        raise
    except:
        print(f"    {Fore.RED}Retrying {Path(filename).name}...{Style.RESET_ALL}")
        raise

    return ret
