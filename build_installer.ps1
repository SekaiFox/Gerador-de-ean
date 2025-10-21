<#
PowerShell helper to build the Inno Setup installer.
Prerequisites:
 - Você deve ter gerado o executável com PyInstaller (dist\GeradorEAN.exe).
 - Instale o Inno Setup (https://jrsoftware.org/isinfo.php) para obter ISCC.exe

Uso (PowerShell):
  .\build_installer.ps1
#>

$ErrorActionPreference = 'Stop'

$distExe = Join-Path -Path (Get-Location) -ChildPath "dist\GeradorEAN.exe"
if (-Not (Test-Path $distExe)) {
    Write-Error "Executável não encontrado: $distExe. Execute o build_exe.ps1 primeiro e verifique que dist\GeradorEAN.exe exista."
    exit 1
}

Write-Host "Procurando ISCC (Inno Setup Compiler)..."
$iscc = Get-Command iscc.exe -ErrorAction SilentlyContinue
if (-not $iscc) {
    # Comuns caminhos de instalação
    $possible = @(
        "$env:ProgramFiles(x86)\Inno Setup 6\ISCC.exe",
        "$env:ProgramFiles\Inno Setup 6\ISCC.exe",
        "$env:ProgramFiles(x86)\Inno Setup 5\ISCC.exe",
        "$env:ProgramFiles\Inno Setup 5\ISCC.exe"
    )
    foreach ($p in $possible) {
        if (Test-Path $p) { $iscc = $p; break }
    }
}

if (-not $iscc) {
    Write-Error "ISCC.exe não encontrado. Instale o Inno Setup: https://jrsoftware.org/isinfo.php"
    exit 1
}

$issPath = Join-Path -Path (Get-Location) -ChildPath "installer.iss"
Write-Host "Compilando instalador com: $iscc`nScript: $issPath"
& $iscc $issPath

if ($LASTEXITCODE -eq 0) { Write-Host "Instalador gerado com sucesso (verifique o diretório do projeto para o arquivo .exe gerado)." } else { Write-Error "Erro ao compilar o instalador (exit code $LASTEXITCODE)" }
