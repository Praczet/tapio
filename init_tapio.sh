#!/usr/bin/env bash

# init_tapio.sh
# Bootstraps the ~/.tapio directory structure with sample placeholders.

set -euo pipefail

# Base directory
BASE_DIR="$HOME/Development/Python/tapio"

# Pet name (optional argument, default 'cat')
PET_NAME="${1:-marvin}"

# Paths
PETS_DIR="$BASE_DIR/pets/$PET_NAME"
FRAMES_DIR="$PETS_DIR/frames"
PLUGINS_DIR="$BASE_DIR/plugins"
NOTIFS_DIR="$BASE_DIR/notifications"
DBUS_DIR="$BASE_DIR/dbus"
DATA_DIR="$BASE_DIR/data/sounds"

# Create directories
mkdir -p "$FRAMES_DIR"
mkdir -p "$PLUGINS_DIR"
mkdir -p "$NOTIFS_DIR"
mkdir -p "$DBUS_DIR"
mkdir -p "$DATA_DIR"

# Create placeholder files
cat >"$PETS_DIR/config.json" <<'EOF'
{
  "name": "${PET_NAME}",
  "animations": [
    "frames/idle.png",
    "frames/walk1.png",
    "frames/sleep.png"
  ],
  "anchor": "bottom-right"
}
EOF

cat >"$NOTIFS_DIR/quotes.json" <<'EOF'
[
  "Hello, world!",
  "Tapio at your service.",
  "Have a great day!"
]
EOF

# Sample DBus service file placeholder
cat >"$DBUS_DIR/org.tapio.DesktopPet.service" <<'EOF'
[D-BUS Service]
Name=org.tapio.DesktopPet
Exec=$BASE_DIR/init_tapio.sh
EOF

# Sample plugin placeholders
cat >"$PLUGINS_DIR/ai_personality.py" <<'EOF'
# ai_personality.py
# Define your AI persona hook here
def register(bot):
    pass
EOF

cat >"$PLUGINS_DIR/calendar_notifier.py" <<'EOF'
# calendar_notifier.py
# Send calendar events to Tapio via DBus or IPC

def register(bot):
    pass
EOF

chmod +x "$BASE_DIR/init_tapio.sh"

echo "Initialized TAPIO structure at $BASE_DIR (pet: $PET_NAME)"
