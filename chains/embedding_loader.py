import json
import pandas as pd
from langchain.schema import Document
from pathlib import Path

def get_documents():
    docs = []
    file_status = {}

    wearable_path = Path("data/wearable_data.csv")
    if wearable_path.exists():
        try:
            df = pd.read_csv(wearable_path)
            for _, row in df.iterrows():
                content = (
                    f"Date: {row['date']}, Steps: {row['steps']}, RHR: {row['resting_hr']} bpm, "
                    f"Light: {row['light_sleep_hours']}h, Deep: {row['deep_sleep_hours']}h, "
                    f"REM: {row['rem_sleep_hours']}h, Total: {row['total_sleep_hours']}h, "
                    f"Tags: {row['tags']}"
                )
                docs.append(Document(page_content=content, metadata={"source": "wearable_data"}))
            file_status["wearable_data.csv"] = f"{len(df)} rows loaded"
        except Exception as e:
            file_status["wearable_data.csv"] = f"Error: {e}"
    else:
        file_status["wearable_data.csv"] = "File not found"

    jsonl_files = [
        "chat_history.jsonl",
        "custom_notes.jsonl",
        "location_data.jsonl",
        "user_profile.jsonl"
    ]

    for file in jsonl_files:
        path = Path(f"data/{file}")
        count = 0
        if path.exists():
            try:
                with open(path, "r", encoding="utf-8") as f:
                    for line in f:
                        data = json.loads(line.strip())
                        content = data.get("text")
                        if content:
                            docs.append(Document(page_content=content, metadata={"source": file}))
                            count += 1
                file_status[file] = f"{count} records loaded"
            except Exception as e:
                file_status[file] = f"Error: {e}"
        else:
            file_status[file] = "File not found"

    docs.append(Document(
        page_content=(
            "Divit P Mallah is a 22-year-old who lives in Chembur, Mumbai. "
            "His sleep goal is to improve REM sleep and reduce morning fatigue. "
            "He is a Night Owl chronotype and uses an Oura Ring and Apple Watch."
        ),
        metadata={"source": "manual_identity"}
    ))
    file_status["manual_identity"] = "Injected"

    print("📂 Data Load Report:")
    for k, v in file_status.items():
        print(f"  - {k}: {v}")

    return docs
