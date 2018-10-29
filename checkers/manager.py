import logging

from .dns import DNSChecker

logger = logging.getLogger(__name__)

def get_prepared_checkers():
    checkers = []
    dns_checker = DNSChecker()
    try:
        dns_checker.startup()
        checkers.append(dns_checker)
    except Exception as e:
        logger.exception("[DNS CHECKER]:Unhandled exception")
        raise e

    return checkers
