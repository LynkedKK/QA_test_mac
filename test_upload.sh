# git config --global user.email "louiscklaw@gmail.com"
# git config --global user.name "louiscklaw"
# git clone https://louiscklaw:$LOUISCKLAW_GITHUB_TOKEN@github.com/LynkedKK/QA_test_result.git --branch=master QA_test_result

cp -r github-actions-ios-emulator-tryout/output_ios14/  QA_test_result/ios14

ls -l QA_test_result

cd QA_test_result
  git add .
  git commit -m"update routine result from ios14,"
  git push
