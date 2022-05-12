# DroneBase Azure Blob Statistics

## Features

-   Reads blob information of folder and results size of each file, total size
-   Date and folder name should be provided on command line

## Tech

Tool uses a number of open source projects to work properly:

-   [azure-storage-blob](https://pypi.org/project/azure-storage-blob/) - Azure SDK
-   [tabulate](https://pypi.org/project/tabulate/) - Table view

## Installation

Tool requires [Python](https://www.python.org/) v3.6+ to run.

Install the dependencies and devDependencies and run the program.

```sh
cd azure_stats
pip3 install -r requirements.txt
python3 stats_gen.py
```

## License

MIT

**Free Software, Hell Yeah!**
