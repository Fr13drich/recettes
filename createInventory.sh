echo "[all]" > inventory
aws ec2 describe-instances \
   --query 'Reservations[*].Instances[*].PublicIpAddress' \
   --filter "Name=tag:Name,Values='recette'" \
   --output text >> inventory
cat inventory
