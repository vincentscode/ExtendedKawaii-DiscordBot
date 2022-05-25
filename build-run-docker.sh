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
 -v $(pwd)/aggressive_config.config.db:/usr/src/app/aggressive_config.config.db \
 -v $(pwd)/rep_ct_config.config.db:/usr/src/app/rep_ct_config.config.db \
 -v $(pwd)/rep_last_config.config.db:/usr/src/app/rep_last_config.config.db \
 -v $(pwd)/sad_config.config.db:/usr/src/app/sad_config.config.db \
 -v $(pwd)/shutup_radio.config.db:/usr/src/app/shutup_radio.config.db \
 -v $(pwd)/source_notify.config.db:/usr/src/app/source_notify.config.db \
 -v $(pwd)/tr_count_user.config.db:/usr/src/app/tr_count_user.config.db \
 -v $(pwd)/txt_count_user.config.db:/usr/src/app/txt_count_user.config.db \
 -v $(pwd)/stammbaum.db3:/usr/src/app/stammbaum.db3 \
 -v $(pwd)/join_leave_log.txt:/usr/src/app/join_leave_log.txt \
 ghcr.io/vincentscode/extendedkawaiibot:latest