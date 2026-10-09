# . Create an abstract class MLModel with:
# • train(data)
# • predict(x)
# • evaluate(test_set)
# Implement models:
# • LinearRegressionModel- some different logic
# • DecisionTreeModel – some logic
# Show how a generic training loop works for any model without caring about details.



from abc import ABC,abstractmethod
class MLModel(ABC):
    