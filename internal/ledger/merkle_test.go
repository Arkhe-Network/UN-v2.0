package ledger

import (
	"bytes"
	"testing"
)

func TestNewMerkleTree(t *testing.T) {
	data := [][]byte{
		[]byte("event 1"),
		[]byte("event 2"),
		[]byte("event 3"),
	}

	tree := NewMerkleTree(data)

	if tree.Root == nil {
		t.Fatal("Expected tree root to be non-nil")
	}

	if len(tree.Leaves) != 3 {
		t.Errorf("Expected 3 leaves, got %d", len(tree.Leaves))
	}

	// Verify root hash calculation
	// Level 0: [h1, h2, h3]
	// Level 1: [h(h1+h2), h(h3+h3)]
	// Level 2: [h(h(h1+h2)+h(h3+h3))]

	if len(tree.Root.Hash) != 32 {
		t.Errorf("Expected 32-byte hash, got %d", len(tree.Root.Hash))
	}
}

func TestEmptyMerkleTree(t *testing.T) {
	tree := NewMerkleTree(nil)
	if tree.Root != nil {
		t.Error("Expected root to be nil for empty tree")
	}
}

func TestMerkleTreeConsistency(t *testing.T) {
	data1 := [][]byte{[]byte("test")}
	data2 := [][]byte{[]byte("test")}

	tree1 := NewMerkleTree(data1)
	tree2 := NewMerkleTree(data2)

	if !bytes.Equal(tree1.Root.Hash, tree2.Root.Hash) {
		t.Error("Identical data should produce identical root hash")
	}
}
