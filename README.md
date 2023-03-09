# Flexport Productivity Infrastructure Take Home

A take home example for an interview


## Running service

```bash
flask --app src/rock_paper_scissors/app  run
```


## Testing service

```bash
curl http://127.0.0.1:5000/health
```

```bash
curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:5000/rps -d '{"move": "Rock"}'
```
