pyinstaller --onefile --windowed -w main.py
mv dist/main .
rm -r build/
rm -r dist/
rm main.spec