import random
import time

def iq_test():
    print("\nWelcome to the IQ Test Simulation!")
    print("I will be your instructor today.")
    print("This test consists of different types of questions to assess your cognitive abilities.")
    print("Please answer carefully. Your time will be recorded.\n")
    
    time.sleep(2)
    print("Test starting in:")
    for i in range(3,0,-1):
        print(f"{i}...")
        time.sleep(1)
    
    score = 0
    start_time = time.time()
    
    # Pattern Questions
    print("\nQuestion 1: Complete the pattern: 2, 4, 8, 16, __")
    ans = input("Your answer: ")
    if ans == "32":
        score += 10
        print("Correct!")
    else:
        print("Incorrect. The answer was 32")

    # Logical Reasoning
    print("\nQuestion 2: If all cats are animals, and some animals are pets,")
    print("which of these statements is definitely true?")
    print("a) All cats are pets")
    print("b) Some cats might be pets")
    print("c) No cats are pets")
    ans = input("Your answer (a/b/c): ").lower()
    if ans == "b":
        score += 10
        print("Correct!")
    else:
        print("Incorrect. The answer was b")

    # Spatial Reasoning
    print("\nQuestion 3: If you rotate a 'b' 180 degrees, what letter do you get?")
    ans = input("Your answer: ").lower()
    if ans == "q":
        score += 10
        print("Correct!")
    else:
        print("Incorrect. The answer was q")

    end_time = time.time()
    time_taken = round(end_time - start_time, 2)

    # Calculate IQ Score (simplified version)
    base_iq = 100
    max_score = 30
    obtained_score = score
    time_factor = min(1.0, 60/time_taken) # Time bonus
    
    final_iq = base_iq + (obtained_score/max_score * 50) * time_factor

    print("\n--- Test Complete ---")
    print(f"Time taken: {time_taken} seconds")
    print(f"Raw score: {score}/30")
    print(f"Estimated IQ Score: {round(final_iq)}")
    
    if final_iq >= 130:
        print("Exceptional performance!")
    elif final_iq >= 110:
        print("Above average performance!")
    elif final_iq >= 90:
        print("Average performance")
    else:
        print("There's room for improvement. Remember, IQ tests don't define your worth!")

if __name__ == "__main__":
    iq_test()
