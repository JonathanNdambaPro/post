import re
import typing as t
import unicodedata

import polars as pl


def lowercase(df: pl.DataFrame, columns: t.Iterable[str]) -> pl.DataFrame:
    return df.with_columns(
        [pl.col(column).str.to_lowercase().alias(column) for column in columns]
    )


def remove_accent(df: pl.DataFrame, columns: t.Iterable[str]) -> pl.DataFrame:
    return df.with_columns(
        [
            pl.col(column)
            .map(
                lambda x: unicodedata.normalize("NFKD", x)
                .encode("ASCII", "ignore")
                .decode("ASCII")
            )
            .alias(column)
            for column in columns
        ]
    )


def replace_special_chars(df: pl.DataFrame, columns: t.Iterable[str]) -> pl.DataFrame:
    return df.with_columns(
        [
            pl.col(column).map(lambda x: re.sub(r"[^\w\s-]", "_", x)).alias(column)
            for column in columns
        ]
    )


def replace_spaces(df: pl.DataFrame, columns: t.Iterable[str]) -> pl.DataFrame:
    return df.with_columns(
        [
            pl.col(column).map(lambda x: re.sub(r"[-\s]+", "_", x)).alias(column)
            for column in columns
        ]
    )


def trim_underscores(df: pl.DataFrame, columns: t.Iterable[str]) -> pl.DataFrame:
    return df.with_columns(
        [pl.col(column).str.strip("_").alias(column) for column in columns]
    )


def round_numbers(
    df: pl.DataFrame, columns: t.Iterable[str], decimals: int
) -> pl.DataFrame:
    return df.with_columns(
        [pl.col(column).round(decimals).alias(column) for column in columns]
    )


def normalize_numbers(df: pl.DataFrame, columns: t.Iterable[str]) -> pl.DataFrame:
    return df.with_columns(
        [
            (
                (pl.col(column) - pl.col(column).min())
                / (pl.col(column).max() - pl.col(column).min())
            ).alias(column)
            for column in columns
        ]
    )


def categorize_age(df: pl.DataFrame, column: str) -> pl.DataFrame:
    return df.with_columns(
        [
            pl.when(pl.col(column) < 18)
            .then("Enfant")
            .when(pl.col(column) < 30)
            .then("Jeune adulte")
            .when(pl.col(column) < 50)
            .then("Adulte")
            .otherwise("Senior")
            .alias(f"{column}_category")
        ]
    )


def main() -> None:
    data = {
        "name": ["Reema", "S'hyam", "Jai", "Nimish'a", "Roh(it", "Riya'e"],
        "gender": ["Femalé", "Male''", "Mal&e", "Female", "Male", "Female"],
        "email": [
            "reema@gmail.com",
            "shyam@yahoo.com",
            "jai@hotmail.com",
            "nimisha@gmail.com",
            "rohit@outlook.com",
            "riyae@gmail.com",
        ],
        "age": [31, 32, 19, 23, 28, 33],
        "salary": [50000.75, 60000.50, 30000.25, 45000.00, 55000.80, 62000.90],
    }

    df = pl.DataFrame(data)

    pipeline = (
        df.pipe(lowercase, columns=["name", "gender", "email"])
        .pipe(remove_accent, columns=["name", "gender"])
        .pipe(replace_special_chars, columns=["name", "gender"])
        .pipe(replace_spaces, columns=["name", "gender"])
        .pipe(trim_underscores, columns=["name", "gender"])
        .pipe(round_numbers, columns=["salary"], decimals=2)
        .pipe(normalize_numbers, columns=["salary"])
        .pipe(categorize_age, column="age")
    )

    print(pipeline)


if __name__ == "__main__":
    main()
