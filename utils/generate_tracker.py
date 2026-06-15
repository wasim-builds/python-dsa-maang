import os
import glob
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRACKER_PATH = os.path.join(BASE_DIR, "TRACKER.md")


def generate_tracker():
    topics_dir = os.path.join(BASE_DIR, "topics")

    if not os.path.exists(topics_dir):
        print("Topics directory not found.")
        return

    tracker_content = [
        "# 📈 Python DSA MAANG Progress Tracker\n",
        "Use this tracker to monitor your progress. You can copy this into Notion or use it directly here.\n",
    ]

    # Get sorted topics
    topics = sorted(
        [
            d
            for d in os.listdir(topics_dir)
            if os.path.isdir(os.path.join(topics_dir, d))
        ]
    )

    total_problems = 0

    for topic in topics:
        topic_path = os.path.join(topics_dir, topic)
        tracker_content.append(f"## {topic.replace('_', ' ').title()}\n")

        # Get difficulties
        difficulties = ["easy", "medium", "hard"]

        for diff in difficulties:
            diff_path = os.path.join(topic_path, diff)
            if not os.path.exists(diff_path):
                continue

            problems = sorted(
                [
                    f
                    for f in os.listdir(diff_path)
                    if f.endswith(".py") and not f.startswith("__")
                ]
            )

            if not problems:
                continue

            tracker_content.append(f"### {diff.capitalize()}\n")

            for prob in problems:
                total_problems += 1
                # Format problem name
                prob_name = prob.replace(".py", "")
                # Capitalize words separated by underscores
                prob_name = " ".join(word.capitalize() for word in prob_name.split("_"))

                # Check if it's a template or real problem (naive check: does it have "Template Problem")
                if "Template Problem" in prob_name:
                    tracker_content.append(f"- [ ] {prob_name} *(Template)*")
                else:
                    tracker_content.append(f"- [ ] **{prob_name}**")

            tracker_content.append("")  # Empty line

    tracker_content.insert(2, f"**Total Problems:** {total_problems}\n")

    with open(TRACKER_PATH, "w") as f:
        f.write("\n".join(tracker_content))

    print(f"✅ Generated tracker at {TRACKER_PATH} with {total_problems} problems.")


if __name__ == "__main__":
    generate_tracker()
