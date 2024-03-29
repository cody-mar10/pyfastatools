from typing import Optional

from pydantic import BaseModel, Field
from pydantic_argparse import ArgumentParser

from fastatools.cli.edit import EditArgs
from fastatools.cli.edit import main as edit_main
from fastatools.cli.split import SplitArgs
from fastatools.cli.split import main as split_main
from fastatools.cli.subset import SubsetArgs
from fastatools.cli.subset import main as subset_main


class Args(BaseModel):
    edit: Optional[EditArgs] = Field(None, description="edit fasta files")
    split: Optional[SplitArgs] = Field(None, description="split fasta files")
    subset: Optional[SubsetArgs] = Field(None, description="subset fasta files")
    # TODO: header methods -> ie extract headers?
    # TODO: stat methods -> print per file stats


def main():
    parser = ArgumentParser(model=Args)
    args = parser.parse_typed_args()

    if args.split is not None:
        split_main(args.split)
    elif args.subset is not None:
        subset_main(args.subset)
    elif args.edit is not None:
        edit_main(args.edit)
