"""
=========================================================
QUANT ULTRA
Main Entry Point
Version : 2.1
=========================================================
"""

import sys
import time

from dotenv import load_dotenv

from validation.system_validator import SystemValidator
from runtime.runtime import Runtime

load_dotenv()


# =========================================================
# Banner
# =========================================================

def banner():

    print()

    print("=" * 80)
    print("🚀 QUANT ULTRA v2.1")
    print("=" * 80)
    print("Starting Quant Ultra Platform...")
    print("=" * 80)


# =========================================================
# Main
# =========================================================

def main():

    banner()

    # -----------------------------------------------------
    # Validate System
    # -----------------------------------------------------

    validator = SystemValidator()

    if not validator.validate():

        print()
        print("❌ System Validation Failed")
        print("Quant Ultra cannot start.")
        sys.exit(1)

    # -----------------------------------------------------
    # Initialize Runtime
    # -----------------------------------------------------

    runtime = Runtime()

    try:

        runtime.initialize()

        config = runtime.get("config")

        print()
        print("=" * 80)
        print("SYSTEM CONFIGURATION")
        print("=" * 80)
        print(f"Profile : {config.profile()}")
        print(f"Capital : {config.get('capital')}")
        print("=" * 80)

        # -------------------------------------------------
        # Start Platform
        # -------------------------------------------------

        runtime.start()

        print()
        print("=" * 80)
        print("✅ Quant Ultra Running...")
        print("Press CTRL + C to stop.")
        print("=" * 80)

        # -------------------------------------------------
        # Keep Main Thread Alive
        # -------------------------------------------------

        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        print()
        print("=" * 80)
        print("🛑 Shutdown Requested")
        print("=" * 80)

    except Exception as e:

        print()
        print("=" * 80)
        print("❌ FATAL ERROR")
        print("=" * 80)
        print(e)
        raise

    finally:

        runtime.stop()

        print()
        print("=" * 80)
        print("✅ Quant Ultra Shutdown Complete")
        print("=" * 80)


# =========================================================

if __name__ == "__main__":

    main()