import bhaptics_python
import asyncio
import time

async def haptic_demo():
    # 1. Initialization
    app_id = "6a6d2b878ff8aa3fd8764770"
    api_key = "DUkpVNUApnpvfISOjc5y"
    app_name = ""

    print("🔧 Initializing bHaptics SDK...")
    result = await bhaptics_python.registry_and_initialize(app_id, api_key, app_name)
    print(f"Initialization result: {result}")

    print("✅ Connected to bHaptics Player.")

    # 2. Check device information
    device_info = await bhaptics_python.get_device_info_json()
    print(f"📱 Connected device info: {device_info}")

    # 3. Test haptic effects
    print("\n🎮 Starting haptic effect tests...")

    # Play dot pattern
    print("• Playing dot pattern")
    values = [50] * 16 + [0] * 16  # Activate first 16 of 32 motors
    await bhaptics_python.play_dot(0, 2000, values)
    await asyncio.sleep(2.5)

    # 4. Cleanup
    await bhaptics_python.stop_all()
    await bhaptics_python.close()
    print("🔚 Demo completed")

# Run the demo
if __name__ == "__main__":
    asyncio.run(haptic_demo())