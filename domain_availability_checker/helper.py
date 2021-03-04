import logging
import whois

logger = logging.getLogger()


def is_domain_available(domain_name: str, total_lines: int, current_count: int) -> bool:
    try:
        domain = whois.query(domain_name)
    except Exception as e:
        logger.warning(f"{current_count}/{total_lines} Checking domain failed: {domain_name}")
        logger.warning(e)
        return False
    if domain:
        logger.info(f"{current_count}/{total_lines} Domain is unavailable: {domain_name}")
        return False
    else:
        # Add query dictionary to available domains
        logger.info(f"{current_count}/{total_lines} Domain is available: {domain_name}")
        return True
