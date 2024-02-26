class Solution {
 void solve(TreeNode*  root, int t,int prev,vector<int>&ty){
        if (root==NULL){
            return;
        }
        
        root->val+=prev;
        if ( root->left==NULL &&root->right==NULL && root->val==t){
            ty.push_back(1);
        }
        
        solve(root->left,t,root->val,ty);
        solve(root->right,t,root->val,ty);
    }
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        vector<int>ty;
        solve(root,targetSum,0,ty);
        // print1(root);
        for (int i=0;i<ty.size();++i){
            cout<<ty[i]<<" ";
            if (ty[i]==1){
                return 1;
            }
            
        }
    return 0;
    }
};
