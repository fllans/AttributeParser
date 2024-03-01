import subprocess
import SearchScada

print(SearchScada.scadaList[0])

# COMPILERS
compilersComponents = []
CfgMaker = subprocess.run(['powershell.exe', r'(Get-Item D:\_Scada_210\Compilers\Cpu850Compiler\CfgMaker.exe).VersionInfo.ProductVersion'], capture_output=True)
HornetLauncher = subprocess.run(['powershell.exe', r'(Get-Item D:\_Scada_210\Compilers\Cpu850Compiler\HornetLauncher.exe).VersionInfo.ProductVersion'], capture_output=True)
ImportZpsClasses = subprocess.run(['powershell.exe', r'(Get-Item D:\_Scada_210\Compilers\Cpu850Compiler\ImportZpsClasses.exe).VersionInfo.ProductVersion'], capture_output=True)
ZpsParser = subprocess.run(['powershell.exe', r'(Get-Item D:\_Scada_210\Compilers\Cpu850Compiler\ZpsParser.exe).VersionInfo.ProductVersion'], capture_output=True)
TAVPLCCompiler = subprocess.run(['powershell.exe', r'(Get-Item D:\_Scada_210\Compilers\TaVplcCompiler\TAVPLCCompiler.exe).VersionInfo.ProductVersion'], capture_output=True)

# print(CfgMaker.stdout.decode())
# print(HornetLauncher.stdout.decode())
# print(ImportZpsClasses.stdout.decode())
# print(ZpsParser.stdout.decode())
# print(TAVPLCCompiler.stdout.decode())


# COMPONENTS
Archive = subprocess.run(['powershell.exe', r'(Get-Item D:\_Scada_210\Scada.Archive\Scada.Archive.exe).VersionInfo.ProductVersion'], capture_output=True)
Client = subprocess.run(['powershell.exe', r'(Get-Item D:\_Scada_210\Scada.Client\scada.exe).VersionInfo.ProductVersion'], capture_output=True)
Server = subprocess.run(['powershell.exe', r'(Get-Item D:\_Scada_210\Scada.Server\Scada.Server.exe).VersionInfo.ProductVersion'], capture_output=True)
TeconWebMonitoring = subprocess.run(['powershell.exe', r'(Get-Item D:\_Scada_210\TeconWebMonitoring\Tecon.Presentation.WebService.exe).VersionInfo.ProductVersion'], capture_output=True)

print(Archive.stdout.decode())
print(Client.stdout.decode())
print(Server.stdout.decode())
print(TeconWebMonitoring.stdout.decode())


# VPLC
Trainer = subprocess.run(['powershell.exe', r'(Get-Item D:\_Scada_210\Scada.VPLC\Trainer\Trainer.exe).VersionInfo.ProductVersion'], capture_output=True)
ManagerServer = subprocess.run(['powershell.exe', r'(Get-Item D:\_Scada_210\Scada.VPLC\ManagerServer\Server.exe).VersionInfo.ProductVersion'], capture_output=True)
ManagerVPLC = subprocess.run(['powershell.exe', r'(Get-Item D:\_Scada_210\Scada.VPLC\ManagerClient\ManagerVPLC.exe).VersionInfo.ProductVersion'], capture_output=True)

# print(Trainer.stdout.decode())
# print(ManagerServer.stdout.decode())
# print(ManagerVPLC.stdout.decode())


# UTILS
ExcelImportExport = subprocess.run(['powershell.exe', r'(Get-Item D:\_Scada_210\Utils\ExcelImportExport\ExcelImportExport.exe).VersionInfo.ProductVersion'], capture_output=True)
GWE2Ex = subprocess.run(['powershell.exe', r'(Get-Item D:\_Scada_210\Utils\GWE2Ex\GWE2Ex.exe).VersionInfo.ProductVersion'], capture_output=True)
slave_104 = subprocess.run(['powershell.exe', r'(Get-Item D:\_Scada_210\Utils\IEC104slave\x64\slave_104.exe).VersionInfo.ProductVersion'], capture_output=True)
ModbusTcpSlave = subprocess.run(['powershell.exe', r'(Get-Item D:\_Scada_210\Utils\ModbusTcpSlave\ModbusTcpSlave.exe).VersionInfo.ProductVersion'], capture_output=True)
Archive_Player = subprocess.run(['powershell.exe', r'(Get-Item D:\_Scada_210\Utils\Scada.Archive.Player\Archive.Player\Archive.Player.exe).VersionInfo.ProductVersion'], capture_output=True)
Archive_Player_Server = subprocess.run(['powershell.exe', r'(Get-Item D:\_Scada_210\Utils\Scada.Archive.Player\Archive.Player.Server\Archive.Player.Server.exe).VersionInfo.ProductVersion'], capture_output=True)
Scada_Monitor_Client = subprocess.run(['powershell.exe', r'(Get-Item D:\_Scada_210\Utils\Scada.Monitor\Scada.Monitor.Client\Scada.Monitor.Client.exe).VersionInfo.ProductVersion'], capture_output=True)
Scada_Monitor_Server = subprocess.run(['powershell.exe', r'(Get-Item D:\_Scada_210\Utils\Scada.Monitor\Scada.Monitor.Server\Scada.Monitor.Server.exe).VersionInfo.ProductVersion'], capture_output=True)
Scada_Opc_TagsSigner = subprocess.run(['powershell.exe', r'(Get-Item D:\_Scada_210\Utils\Scada.Opc.TagsSigner\Scada.Opc.TagsSigner.exe).VersionInfo.ProductVersion'], capture_output=True)
Scada_Opc_TcpProxy = subprocess.run(['powershell.exe', r'(Get-Item D:\_Scada_210\Utils\Scada.Opc.TcpProxy\Scada.Opc.TcpProxy.exe).VersionInfo.ProductVersion'], capture_output=True)
Scada_Server_DataMirror = subprocess.run(['powershell.exe', r'(Get-Item D:\_Scada_210\Utils\Scada.Server.DataMirror\Scada.Server.DataMirror.exe).VersionInfo.ProductVersion'], capture_output=True)
SiriusCompiler = subprocess.run(['powershell.exe', r'(Get-Item D:\_Scada_210\Utils\SiriusCompiler\SiriusCompiler.exe).VersionInfo.ProductVersion'], capture_output=True)
UpsServer = subprocess.run(['powershell.exe', r'(Get-Item D:\_Scada_210\Utils\UpsServer\StandartUpsManager.exe).VersionInfo.ProductVersion'], capture_output=True)

# print(ExcelImportExport.stdout.decode())
# print(GWE2Ex.stdout.decode())
# print(slave_104.stdout.decode())
# print(ModbusTcpSlave.stdout.decode())
# print(Archive_Player.stdout.decode())
# print(Archive_Player_Server.stdout.decode())
# print(Scada_Monitor_Client.stdout.decode())
# print(Scada_Monitor_Server.stdout.decode())
# print(Scada_Opc_TagsSigner.stdout.decode())
# print(Scada_Opc_TcpProxy.stdout.decode())
# print(Scada_Server_DataMirror.stdout.decode())
# print(SiriusCompiler.stdout.decode())
# print(UpsServer.stdout.decode())