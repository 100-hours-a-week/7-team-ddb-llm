# pip install -U datasets fsspec

from datasets import load_dataset

# JSONL 파일 경로
jsonl_file = "./output.jsonl"

# JSONL 파일을 Dataset으로 로드
dataset = load_dataset("json", data_files=jsonl_file, download_mode="force_redownload")


# 허브에 업로드 하는 코드 (colab에서 실행)
# from huggingface_hub import HfApi
# from google.colab import userdata

# # HfApi 인스턴스 생성
# api = HfApi()

# # 데이터셋을 업로드할 리포지토리 이름
# repo_name = "chanhue/dolpin"

# # 데이터셋을 허브에 푸시
# dataset.push_to_hub(repo_name, token=userdata.get('HUGGING_FACE'))

# 허브에 업로드 하는 코드 (local에서 실행 .env 파일 필요)
from huggingface_hub import HfApi
from dotenv import load_dotenv
import os

# .env 파일에서 환경변수 불러오기
load_dotenv()

# 환경변수에서 토큰 가져오기
token = os.getenv('HUGGING_FACE')

# 데이터셋을 허브에 푸시
dataset.push_to_hub(repo_name, token=token)


from huggingface_hub import snapshot_download

snapshot_download(repo_id="chanhue/dolpin", repo_type="dataset")
