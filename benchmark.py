from rich.console import Console

from config import DNS_SERVERS
from config import DOMAINS

console=Console()

def main():

    console.rule("[bold green]DNS Benchmark")

    console.print()

    console.print(f"Resolvers : {len(DNS_SERVERS)}")

    console.print(f"Domains   : {len(DOMAINS)}")

    console.print()

    console.print("Benchmark engine not yet implemented.")

if __name__=="__main__":
    main()