class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
        vector<vector<int >>ans;
        if(root==NULL){
            return 0;
        }
        queue<TreeNode * >res;
        res.push(root);
        
        while(!res.empty()){
            int size = res.size();
            vector<int>kl;
            
            for (int i=0;i<size;++i){
                TreeNode* node= res.front();
                res.pop();
                if(node->left!=NULL){
                    res.push(node->left);
                }
                if(node->right!=NULL){
                    res.push(node->right);
                }
                kl.push_back(node->val);
            }
            ans.push_back(kl);
        }
        int yupp=ans.size()-1;
        int bb=0;
        for (int i=0;i<ans[yupp].size();++i){
            bb=ans[yupp][0];
        }
        return bb;
    }
};
