; Inno Setup script to create an installer for GeradorEAN
; Usage: open this file in Inno Setup or run ISCC.exe installer.iss

[Setup]
AppName=Gerador EAN
AppVersion=1.0
DefaultDirName={pf64}\GeradorEAN
DefaultGroupName=Gerador EAN
OutputBaseFilename=GeradorEAN_Installer
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64

[Languages]
Name: "portuguese"; MessagesFile: "compiler:Languages\Portuguese.isl"

[Files]
; include the already built executable from dist\GeradorEAN.exe
Source: "{#DistExe}"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Gerador EAN"; Filename: "{app}\GeradorEAN.exe"
Name: "{userdesktop}\Gerador EAN"; Filename: "{app}\GeradorEAN.exe"; Tasks: desktopicon

[Tasks]
Name: desktopicon; Description: "Criar ícone na área de trabalho"; GroupDescription: "Opções de instalação:"; Flags: unchecked

[Run]
Filename: "{app}\GeradorEAN.exe"; Description: "Abrir Gerador EAN"; Flags: nowait postinstall skipifsilent

; Define a constant with the expected path of the dist executable - replaced at build time
#define DistExe "dist\\GeradorEAN.exe"
