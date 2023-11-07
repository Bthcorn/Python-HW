def print_btree_recursive(node, depth=0):
    if node is not None:
        print("." * depth + node[0])
        for child in node[1:]:
            print_btree_recursive(child, depth + 1)

# Example usage
tree = ["1",
        ["11",
            ["111"],
            ["112"]
        ],
        ["12",
            ["121",
                ["122",
                    ["1221"],
                    ["1222"]
                ]
            ]
        ]
       ]

print_btree_recursive(tree)
