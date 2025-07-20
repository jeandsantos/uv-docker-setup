from uv_setup.main import main


class TestMain:
    def test_main(self, capsys):
        result = main()

        assert result is None, "Main function should not return anything"

        captured = capsys.readouterr()
        assert "Hello from uv-setup!" in captured.out, "Output should contain greeting"
