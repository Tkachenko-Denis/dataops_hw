# hw_15

## Chart

`hello-world-chart` deploys the `hw_13` FastAPI service with configurable:

- image tag
- cpu/memory requests and limits
- ingress manifest generation

## Example commands

```powershell
helm install hw15-default .\hello-world-chart
helm install hw15-noingress .\hello-world-chart -f .\hello-world-chart\values-no-ingress.yaml
helm install hw15-scaled .\hello-world-chart -f .\hello-world-chart\values-scaled.yaml
```
