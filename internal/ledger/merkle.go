package ledger

import (
	"crypto/sha256"
)

// Node represents a node in the Merkle Tree.
type Node struct {
	Hash []byte
}

// MerkleTree represents a verifiable audit trail structure.
type MerkleTree struct {
	Root  *Node
	Leaves []*Node
}

// NewMerkleTree creates a new Merkle Tree from a list of data using an iterative approach.
func NewMerkleTree(data [][]byte) *MerkleTree {
	var leaves []*Node
	for _, d := range data {
		hash := sha256.Sum256(d)
		leaves = append(leaves, &Node{Hash: hash[:]})
	}

	if len(leaves) == 0 {
		return &MerkleTree{}
	}

	root := buildTreeIterative(leaves)
	return &MerkleTree{
		Root:   root,
		Leaves: leaves,
	}
}

func buildTreeIterative(nodes []*Node) *Node {
	currentLevel := nodes
	for len(currentLevel) > 1 {
		var nextLevel []*Node
		for i := 0; i < len(currentLevel); i += 2 {
			if i+1 < len(currentLevel) {
				hash := sha256.Sum256(append(currentLevel[i].Hash, currentLevel[i+1].Hash...))
				nextLevel = append(nextLevel, &Node{Hash: hash[:]})
			} else {
				// Handle odd number of nodes by duplicating the last one (common Merkle strategy)
				hash := sha256.Sum256(append(currentLevel[i].Hash, currentLevel[i].Hash...))
				nextLevel = append(nextLevel, &Node{Hash: hash[:]})
			}
		}
		currentLevel = nextLevel
	}
	return currentLevel[0]
}
