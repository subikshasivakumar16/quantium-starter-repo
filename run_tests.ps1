# Activate virtual environment
& .\venv\Scripts\Activate.ps1

# Run pytest
pytest tests/test_app.py

# Check exit code
if ($LASTEXITCODE -eq 0) {
    Write-Output "All tests passed!"
    exit 0
} else {
    Write-Output "Some tests failed!"
    exit 1
}
