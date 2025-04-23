/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
 /*
 URL := https://leetcode.com/problems/binary-search-tree-iterator/description/
 173. Binary Search Tree Iterator

Intuition & Approach :
1. Prealloc phase -> exec inOrder ( left,root, right ) traversal. 
2. Store a pointer to a current element : O(1) to move a pointer
3. Safety check in class initializer ( no garbage memory issues at runtime )

 */
class BSTIterator {
public:
    std::vector<TreeNode*> data = std::vector<TreeNode*>();
    int nodePtr = 0;
    int length = 0;

    BSTIterator(TreeNode* root) {
        dfs(root);
        this->length = this->data.size();
    }

    //  could store ints, BUT, better to store everything
    void dfs(TreeNode* root) {
        if(root->left != NULL){
            dfs(root->left);
        }
        this->data.push_back(root);
        if(root->right != NULL){
            dfs(root->right);
        }
    }
    
    int next() {
        TreeNode* curNode = this->data[this->nodePtr];
        this->nodePtr = this->nodePtr + 1;
        int targetVal = curNode->val;
        return targetVal;
    }
    
    bool hasNext() {
        return (this->nodePtr < this->length);
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
