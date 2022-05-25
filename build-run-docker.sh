# docker build -t ghcr.io/vincentscode/extendedkawaiibot:latest .
docker pull ghcr.io/vincentscode/extendedkawaiibot:latest

docker run --rm --name extendedkawaiibot-test -d \
 -v $(pwd)/config.py:/usr/src/app/config.py \
 -v $(pwd)/assets:/usr/src/app/assets \
 -v $(pwd)/logs:/usr/src/app/logs \
 -v $(pwd)/cache:/usr/src/app/cache \
 -v $(pwd)/server_actions:/usr/src/app/server_actions \
 -v $(pwd)/server_proposed_actions:/usr/src/app/server_proposed_actions \
 -v $(pwd)/server_webhooks:/usr/src/app/server_webhooks \
 -v $(pwd)/messages_per_day_cache:/usr/src/app/messages_per_day_cache \
 ghcr.io/vincentscode/extendedkawaiibot:latest
