## Speedtest CLI for Docker

### **Pull image:**
```bash
docker pull ghcr.io/volkovskiyda/speedtest
```

### **Run container:**
```bash
docker run --rm ghcr.io/volkovskiyda/speedtest
```

### **Run container with bash entrypoint:**
```bash
docker run -it --rm --entrypoint bash ghcr.io/volkovskiyda/speedtest
> python speedtest.py
# or
> bash run.sh
```

### **Speedtest cli help:**
```bash
docker run -it --rm --entrypoint speedtest ghcr.io/volkovskiyda/speedtest -h
```
