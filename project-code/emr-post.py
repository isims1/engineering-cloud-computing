import subprocess

def emr_post(num_nodes):

   aws_cmd = "aws emr create-cluster --name=\'E516-JupyterHub-Cluster\'"
   aws_cmd = aws_cmd + " --release-label emr-5.19.0"
   aws_cmd = aws_cmd + " --applications Name=JupyterHub"
   aws_cmd = aws_cmd + " --log-uri s3://e516-jupyterhub-backup/JupyterClusterLogs"
   aws_cmd = aws_cmd + " --use-default-roles"
   aws_cmd = aws_cmd + " --ec2-attributes SubnetIds=subnet-d0169eaa,KeyName=dlec2-key,AdditionalMasterSecurityGroups=[\'sg-01c1d97ca12d1f2e7\']"
   aws_cmd = aws_cmd + " --instance-count " + str(num_nodes)
   aws_cmd = aws_cmd + " --instance-type m4.large"
   aws_cmd = aws_cmd + " --configurations \'[{\"Classification\":\"jupyter-s3-conf\",\"Properties\":{\"s3.persistence.bucket\":\"e516-jupyter-backup\",\"s3.persistence.enabled\":\"true\"},\"Configurations\":[]}]\'"
   aws_cmd = aws_cmd + " --output text"

   c_id = subprocess.run(aws_cmd, shell=True, stdout=subprocess.PIPE)

   cid = c_id.stdout.decode('utf-8')
   cid = cid.rstrip()

   c_status = "http://ec2-18-191-50-79.us-east-2.compute.amazonaws.com:8080/api/emr/info/" + cid
   t_clstr = 'curl -X "DELETE" http://ec2-18-191-50-79.us-east-2.compute.amazonaws.com:8080/api/emr/terminate/' + cid

   rtn_dict = {
      "ClusterId": cid,
      "CheckClusterStatus": c_status,
      "TerminateCluster": t_clstr
   }

   return rtn_dict


print(emr_post(2))
