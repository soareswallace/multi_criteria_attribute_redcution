def instance_correctly_classified_by_both(instance):
    return (instance.get_instance_class() == instance.get_prediction_class_using_whole_attributes()) and\
           (instance.get_instance_class() == instance.get_prediction_class_using_reduced_attributes())

def instance_correctly_classified_only_by_AT(instance):
    return (instance.get_instance_class() == instance.get_prediction_class_using_whole_attributes()) and\
           not (instance.get_instance_class() == instance.get_prediction_class_using_reduced_attributes())

def instance_correctly_classified_only_by_A(instance):
    return not (instance.get_instance_class() == instance.get_prediction_class_using_whole_attributes()) and\
           (instance.get_instance_class() == instance.get_prediction_class_using_reduced_attributes())

def compute_ndc_attributes(instaces_info):
    a = 0
    b = 0
    c = 0
    d = 0

    for instace in instaces_info:
        if instance_correctly_classified_by_both(instace):
            a += 1
        elif instance_correctly_classified_only_by_AT(instace):
            b += 1
        elif instance_correctly_classified_only_by_A(instace):
            c += 1
        else:
            d += 1

    return a, b, c, d