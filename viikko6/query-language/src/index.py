from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or
from query_builder import QueryBuilder

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    # matcher = query.build()

    # for player in stats.matches(matcher):
    #     print(player)

    # print()

    # query = QueryBuilder()

    # matcher = query.playsIn("NYR").build()

    # for player in stats.matches(matcher):
    #     print(player)

    # print()
    m1 = (
    query
        .playsIn("PHI")
        .hasAtLeast(10, "assists")
        .hasFewerThan(5, "goals")
        .build()
    )

    m2 = (
    query
        .playsIn("EDM")
        .hasAtLeast(40, "points")
        .build()
    )

    matcher = query.oneOf(m1, m2).build()
    # query = QueryBuilder()

    # matcher = query.playsIn("NYR").hasAtLeast(5, "goals").hasFewerThan(10, "goals").build()

    for player in stats.matches(matcher):
        print(player)

    # matcher = And(
    #     HasAtLeast(5, "goals"),
    #     HasAtLeast(5, "assists"),
    #     PlaysIn("PHI")
    # )

    # for player in stats.matches(matcher):
    #     print(player)

    # matcher = Or(
    #     HasAtLeast(30, "goals"),
    #     HasAtLeast(50, "assists")
    # )

    # for player in stats.matches(matcher):
    #     print(player)

    # print()

    # matcher = And(
    #     HasAtLeast(40, "points"),
    #     Or(
    #         PlaysIn("NYR"),
    #         PlaysIn("NYI"),
    #         PlaysIn("BOS")
    #     )
    # )

    # for player in stats.matches(matcher):
    #     print(player)

if __name__ == "__main__":
    main()
