#!/usr/bin/env python3

if __name__ == "__main__":
    import codebase_rag.constants
    import codebase_rag.config

    codebase_rag.constants.OLLAMA_DEFAULT_BASE_URL = "https://api.siliconflow.cn"
    codebase_rag.config.settings.MEMGRAPH_HOST = "host.docker.internal"

    from codebase_rag.cli import app
    app()
