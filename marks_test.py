import marks

def test_1(monkeypatch, capsys):
    inputs = iter(['4','5','4','0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    marks.main()
    captured = capsys.readouterr()
    assert captured.out == ('Notenschnitt: 4.5\n')

def test_2(monkeypatch, capsys):
    inputs = iter(['3.5','5.5','0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    marks.main()
    captured = capsys.readouterr()
    assert captured.out == ('Notenschnitt: 5.5\n')

def test_3(monkeypatch, capsys):
    inputs = iter(['4.75','0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    marks.main()
    captured = capsys.readouterr()
    assert captured.out == ('Notenschnitt: 4.75\n')