import logging

logging.basicConfig(
    level=logging.WARNING,
    format="%(module)s--%(lineno)d - %(asctime)s: %(message)s",
    filename='test log.txt',  
)

log = logging.getLogger(__name__)

def divide(first_num:float, second_num:float)->float:
    log.info(f'So thu nhat la: {first_num}')
    log.info(f'So thu hai la: {second_num}')
    result = first_num/second_num
    return result

result = divide(10,5)
log.debug(f'Gia tri la: {result}')