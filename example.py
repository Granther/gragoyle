import bhaptics_python
import asyncio
import time

async def init():
    app_id = "69bf315ab739d9e6b1942b96"
    api_key = "vImyGPE7pBD74cWjJ4mm"
    app_name = "lang1"
    
    print("🔧 Initializing bHaptics SDK...")
    result = await bhaptics_python.registry_and_initialize(app_id, api_key, app_name)
    print(f"Initialization result: {result}")
    
    print("✅ Connected to bHaptics Player.")
    
    # 2. Check device information
    device_info = await bhaptics_python.get_device_info_json()
    print(f"📱 Connected device info: {device_info}")
    
    # 3. Test haptic effects
    print("\n🎮 Starting haptic effect tests...") 

async def short_sentence():
    await init()

    import random

    nouns = ["dog", "cat", "hospital", "office", "court", "person"]
    verbs = ["vring", "glorping", "modeling", "programming"]

    while True:
        verbn, nounn = random.randint(0, 3), random.randint(0, 5)

        verb = verbs[verbn]+"_lang1"
        noun = nouns[nounn]+"_lang1"

        await bhaptics_python.play_event(event_name=noun)
        await asyncio.sleep(1.2)

        await bhaptics_python.play_event(event_name=verb)
        await asyncio.sleep(1.2)

        guess = input("Guess: ")
        sent = nouns[nounn] + " " + verbs[verbn]
        if guess == sent:
            print("Right!")
        else:
            print("Wrong! It was: ", sent)

        time.sleep(1)
    
    return

async def noun_quiz():
    await init()
    
    import random

    nouns = ["dog", "cat", "hospital", "office", "court", "person"]

    while True:
        nounn = random.randint(0, 5)
        noun = nouns[nounn]+"_lang1"

        await bhaptics_python.play_event(event_name=noun)
        await asyncio.sleep(1.2)

        guess = input("Guess: ")
        word = nouns[nounn]
        if guess == word:
            print("Right!")
        else:
            print("Wrong! It was: ", word)

        time.sleep(1)

async def all_quiz():
    await init()
    
    import random

    nouns = ["dog", "cat", "hospital", "office", "court", "person"]
    verbs = ["vring", "glorping", "modeling", "programming"]
    alls = nouns + verbs

    while True:
        randn = random.randint(0, len(nouns) + len(verbs)-1)
        noun = alls[randn]+"_lang1"

        await bhaptics_python.play_event(event_name=noun)
        await asyncio.sleep(1.2)

        guess = input("Guess: ")
        word = alls[randn]
        if guess == word:
            print("Right!")
        else:
            print("Wrong! It was: ", word)

        time.sleep(1)

async def haptic_demo():
    
    values = [10] * 40

    for word in sentence:
        await bhaptics_python.play_event(event_name=word)
        await asyncio.sleep(1)
        print("playing: ", word)

    return

    print("Playing event")
    await bhaptics_python.play_event(event_name="test1")
    await asyncio.sleep(1)
    await bhaptics_python.play_dot(0, 500, values)

    return

    # Play dot pattern
    print("• Playing dot pattern")
    values = [10] * 40  # Activate first 16 of 32 motors
    print(values)
    await bhaptics_python.play_dot(0, 500, values)
    await asyncio.sleep(0.5)
    
    # Play path pattern
    print("• Playing path pattern")
    x = [0.2]
    y = [0.4]
    intensity = [80]
    await bhaptics_python.play_path(0, 3000, x, y, intensity)
    await asyncio.sleep(3.5)
    
    # 4. Cleanup
    await bhaptics_python.stop_all()
    await bhaptics_python.close()
    print("🔚 Demo completed")

# Run the demo
if __name__ == "__main__":
    #asyncio.run(haptic_demo())
    asyncio.run(short_sentence())
    #asyncio.run(noun_quiz())
    #asyncio.run(all_quiz())