import pytest
from day3 import buildframe, get_series, answer2, answer1


class Test:
    @pytest.fixture()
    def target(self):
        return "#"

    @pytest.fixture()
    def teststring(self):
        teststring = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
        return teststring

    @pytest.fixture()
    def slope(self):
        slope = (3, 1)
        return slope

    @pytest.fixture()
    def nrows(self, slope, teststring):
        return buildframe(slope, teststring)

    @pytest.fixture()
    def firstanswer(self):
        return 7

    @pytest.fixture()
    def secondanswer(self):
        return 336

    @pytest.fixture()
    def slopes(self):
        return [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    def test_buildframe(self, teststring, slope):
        rowcount = len(teststring.split("\n"))
        frame = buildframe(slope, teststring)
        assert frame.shape[0] == rowcount

    def test_get_series(self, slope, nrows):
        series = get_series(slope=slope, nrows=nrows)
        assert len(series) == nrows.shape[0] / slope[1]

    def test_answer1(self, teststring, slope, target, firstanswer):
        a1 = answer1(datastring=teststring, slope=slope, target=target)
        assert a1 == firstanswer

    def test_answer2(self, slope, target, secondanswer, teststring, slopes):
        assert (
            answer2(slopes=slopes, datastring=teststring, target=target) == secondanswer
        )
