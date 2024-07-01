import os
import sys
import random
import pytest
from datetime import datetime

# interesting note - the main source code to see how PyTest works is in the dunder folders...
from _pytest.nodes import Item
from _pytest.runner import CallInfo
from pyboxen import boxen
from rich.console import Console

console = Console()


# ----- Command Line Arguments -----
def pytest_addoption(parser):
    parser.addoption(
        "--desc", action="store_true", default=False, help="sort descending"
    )
    parser.addoption("--asc", action="store_true", default=False, help="sort ascending")
    parser.addoption(
        "--folder", action="store_true", default=False, help="sort by folder"
    )
    parser.addoption(
        "--id_desc", action="store_true", default=False, help="sort by test id desc"
    )
    parser.addoption(
        "--id", action="store_true", default=False, help="sort by test id asc"
    )
    parser.addoption("--rnd", action="store_true", default=False, help="randomise")
    parser.addoption(
        "--collect", action="store_true", default=False, help="coolect only"
    )


# ----- GLOBAL VALUES -----
def pytest_configure(config):

    config.my_global_value = "✅ MY GLOBLAL VALUE ✅"


# report is report for a single test
# @pytest.hookimpl
def pytest_report_teststatus(report, config):
    # order seems to matter as the xpassed did not work when placed after passed
    # Handle xfailed and xpassed
    # https://github.com/Teemu/pytest-sugar/blob/main/pytest_sugar.py#L221
    if hasattr(report, "wasxfail"):
        if report.skipped:
            # short desc, long desc
            return "xfailed", "x", ("XFAIL ✅")
        elif report.passed:
            return "xpassed", "❌", ("XPASS ✅❌")
        else:
            return "", "", ""
    if report.when in ("setup", "teardown", "call") and report.skipped:
        return report.outcome, "s", "SKIPPED 🙄 "
    if report.when == "call" and report.passed:
        # we can style the text in long formats. Just color and bold no italic
        # does not work for error?
        return report.outcome, "T", ("PASSED ✅", {"green": True, "bold": True})
    if report.when == "call" and report.failed:
        return report.outcome, "E", ("FAILED ❌")  # changed from recording


def pytest_report_header(config):
    if config.getoption("verbose") > 0:
        output = "📝 ✅ pytest_report_header ❌"
        print(
            boxen(
                output,
                title="[blue]We can add a report header[/] [black on cyan] here... [/]",
                subtitle="pytest_report_header",
                subtitle_alignment="left",
                color="green",
                padding=1,
            )
        )
        # We can add another item the report header but it is useful to see that we get a return value that automatically gets added to the terminal report
        return [
            f"\n📝 This is in a pytest_report_header hook and it can access the config built in fixture: {config.my_global_value}"
        ]


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    reports = terminalreporter.getreports("")
    # this holds record_property custom data
    # output = [report.user_properties for report in reports]
    # output2 = [report.sections for report in reports]
    # content is truthy only if record properties have been set
    content = os.linesep.join(
        f"{key}: {value}" for report in reports for key, value in report.user_properties
    )
    # console.print(content)
    if content:
        # https://docs.pytest.org/en/7.1.x/reference/reference.html?highlight=record_property#std-fixture-record_property
        terminalreporter.ensure_newline()
        terminalreporter.section("RECORD PROPERTY", sep="-", red=True, bold=True)
        terminalreporter.line(content)
        print("\n")
        terminalreporter.ensure_newline()
        terminalreporter.section(
            f"Our custom test results section with exit status: {exitstatus}",
            sep="=",
            blue=True,
            bold=True,
            fullwidth=None,
        )
    # change from video - this runs regardless of content having a value
    # content may be empty if no record properties have been set so we have moved this out of the `if content
    print("\n")
    passed_tests = len(terminalreporter.stats.get("passed", ""))
    failed_tests = len(terminalreporter.stats.get("failed", ""))
    skipped_tests = len(terminalreporter.stats.get("skipped", ""))
    error_tests = len(terminalreporter.stats.get("error", ""))
    xfailed_tests = len(terminalreporter.stats.get("xfailed", ""))
    xpassed_tests = len(terminalreporter.stats.get("xpassed", ""))

    total_tests = (
        passed_tests
        + failed_tests
        + skipped_tests
        + error_tests
        + xfailed_tests
        + xpassed_tests
    )

    output = f"Total tests: {total_tests}\n"
    output += f"Passed: {passed_tests}\n"
    output += f"Failed: {failed_tests}\n"
    output += f"Skipped: {skipped_tests}\n"
    output += f"Error: {error_tests}\n"
    output += f"xfailed: {xfailed_tests}\n"
    output += f"xpassed: {xpassed_tests}\n"
    print(
        boxen(
            output,
            title="[green]START OF TEST RESULTS[/]",
            title_alignment="center",
            subtitle="END OF TEST RESULTS",
            subtitle_alignment="center",
            color="green",
            padding=1,
        )
    )
