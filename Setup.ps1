Write-Host "Cleaning artifacts"
rm dist -Force -ErrorAction Ignore
rm 	cash.egg-info -Force -ErrorAction Ignore
rm cash/__pycache__ -Force -ErrorAction Ignore
Write-Host "Building"
poetry build
Write-Host "Installing"
$file = Get-ChildItem -Path .\dist\ -Recurse -Include *.tar.gz
pip3 install $file
Write-Host "Ok cool"
