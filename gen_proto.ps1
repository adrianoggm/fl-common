# fl-common\gen_proto.ps1
param(
    [string]$ProtoDir = "$PSScriptRoot\proto",
    [string]$OutDir   = "$PSScriptRoot\src"
)

Write-Host "Generando stubs gRPC desde $ProtoDir hacia $OutDir …"

python -m grpc_tools.protoc `
  -I"$ProtoDir" `
  --python_out="$OutDir" `
  --grpc_python_out="$OutDir" `
  "$ProtoDir\model.proto"

Write-Host "¡Stubs generados satisfactoriamente!"
