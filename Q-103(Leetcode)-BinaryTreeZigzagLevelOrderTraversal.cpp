class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>>res;
        if(root==NULL){
            return res;
        }
        queue<TreeNode*>q;
        q.push(root);
        while(!q.empty()){
            vector<int>trial;
            int size=q.size();
            for(int i=0;i<size;i++){
                TreeNode* node=q.front();
                q.pop();
                if (node->left!=NULL){
                    q.push(node->left);
                }
                if (node->right!=NULL){
                    q.push(node->right);
                }
                trial.push_back(node->val);
            }
            res.push_back(trial);
        }
        int n=res.size();
        for (int i=0;i<res.size();++i){
            vector<int>yu;
            if (i%2!=0){
                for (int k=res[i].size()-1;k>=0;k--){
                        yu.push_back(res[i][k]);
                }
                res[i]=yu;
            }
        }
        return res;
    }
};
