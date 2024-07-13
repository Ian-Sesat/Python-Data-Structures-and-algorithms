class TreeNode:
    def __init__(self, name,designation):
        self.name = name
        self.designation=designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self,choice):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if choice=='name':
            print(prefix + self.name)
        elif choice=='designation':
            print(prefix + self.designation)
        elif choice=='both':
            print(prefix+self.name+' ({})'.format(self.designation))
        if self.children:
            for child in self.children:
                child.print_tree(choice)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_management_tree():
    root = TreeNode('Nilupul','CEO')

    chinmay = TreeNode('Chinmay','CTO')
    vishwa=TreeNode( 'Vishwa','Infrastructure Head')
    dhaval=TreeNode('Dhaval','Cloud Manager')
    vishwa.add_child(dhaval)
    abhijit=TreeNode('Abhijit','App Manager')
    vishwa.add_child(abhijit)
    amir=TreeNode('Amir','Application Head')

    chinmay.add_child(vishwa)
    chinmay.add_child(amir)
 
    gels= TreeNode('Gels','HR Head')
    peter=TreeNode('Peter','Recruitment Manager')
    gels.add_child(peter)
    waqas=TreeNode('Waqas','Policy Manager')
    gels.add_child(waqas)
    
    root.add_child(chinmay)
    root.add_child(gels)

    return root
def main():
    root=build_management_tree()
    root.print_tree('name')
    root.print_tree('designation')
    root.print_tree('both')

if __name__ == '__main__':
    main()