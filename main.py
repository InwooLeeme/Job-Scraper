from wwr import extract_wwr
from remoteok import extract_remoteok
from stackover import extract_stackover

wwr_result = extract_wwr()

remoteok_result = extract_remoteok()

stackover_result = extract_stackover()

print(stackover_result)
