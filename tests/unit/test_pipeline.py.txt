from waxs_cellulose.pipeline import run_pipeline


def test_pipeline_runs(tmp_path):
    file = tmp_path / "data.txt"
    file.write_text("0 1\n1 2\n2 3")

    result = run_pipeline(str(file))
    assert result is not None