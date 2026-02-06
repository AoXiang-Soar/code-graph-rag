from codebase_rag.cli import start
from codebase_rag.config import settings
from codebase_rag.main import connect_memgraph

d4j_list_of_bugs = [("Chart", [i for i in range(1, 27)]),
                        ("Cli", [i for i in range(1, 41) if i not in [6]]),
                        ("Closure", [i for i in range(1, 177) if i not in [63, 93]]),
                        ("Codec", [i for i in range(1, 19)]),
                        ("Collections", [i for i in range(1, 29)]),
                        ("Compress", [i for i in range(1, 48)]),
                        ("Csv", [i for i in range(1, 17)]),
                        ("Gson", [i for i in range(1, 19)]),
                        ("JacksonCore", [i for i in range(1, 27)]),
                        ("JacksonDatabind", [i for i in range(1, 113) if i not in [65, 89]]),
                        ("JacksonXml", [i for i in range(1, 7)]),
                        ("Jsoup", [i for i in range(1, 94)]),
                        ("JxPath", [i for i in range(1, 23)]),
                        ("Lang", [i for i in range(1, 66) if i not in [2, 18, 25, 48]]),
                        ("Math", [i for i in range(1, 107)]),
                        ("Mockito", [i for i in range(1, 39)]),
                        ("Time", [i for i in range(1, 28) if i not in [21]])]

for project, bugs in d4j_list_of_bugs:
    for bug in bugs:
        start(repo_path=f'/d4j/{project}-{bug}', update_graph=True, clean=True)
        effective_batch_size = settings.resolve_batch_size(None)
        with connect_memgraph(effective_batch_size) as ingestor:
            ingestor.execute_write(f'CALL export_util.json("/export/{project}-{bug}.json") YIELD export_util;')

