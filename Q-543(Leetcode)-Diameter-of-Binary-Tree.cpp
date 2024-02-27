class Solution {
    public:
    int height(TreeNode* root){
        if(root == NULL)
        return 0;
        int ans = max(height(root->left),height(root->right)) +1;
        return ans;
    }
   
    int diameterOfBinaryTree(TreeNode* root) {
        if(root == NULL)
            return 0;
        int opt1 = diameterOfBinaryTree(root->left);
        int opt2 = diameterOfBinaryTree(root->right);
        int opt3 = height(root->left) + height(root->right); 
        
        int ans  = max(opt3,max(opt1,opt2));
        // cout<<root->val << " "<<ans<<endl;
        return ans;
    }
};
